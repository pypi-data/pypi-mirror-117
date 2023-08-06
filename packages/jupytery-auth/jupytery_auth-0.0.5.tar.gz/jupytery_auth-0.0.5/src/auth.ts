import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { LabIcon } from '@jupyterlab/ui-components';
import peopleSvg from './../style/icons/people-24px.svg';
import { requestAPI } from './handler'
import AuthWidget from './widget';

import '../style/index.css';

function request(path: string, widget: AuthWidget) {
  return requestAPI<any>(path)
    .then(data => {
      console.log('Got a response from the jupytery_auth server API', data);
      widget.setUsers(data);
      // @ts-ignore
      window.juser = data
    })
    .catch(reason => {
      console.log('The jupytery_auth server API appears to be missing', reason);
    });
}

export const peopleIcon = new LabIcon({
  name: 'auth:users',
  svgstr: peopleSvg
});

const auth: JupyterFrontEndPlugin<void> = {
  id: '@datalayer-jupyter/auth',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    const widget = new AuthWidget();
    widget.id = '@datalayer-jupyter/auth'
    widget.title.icon = peopleIcon;
    app.shell.add(widget, 'left', { rank: 300 })
    request('users', widget)
  }

};

export default auth;
