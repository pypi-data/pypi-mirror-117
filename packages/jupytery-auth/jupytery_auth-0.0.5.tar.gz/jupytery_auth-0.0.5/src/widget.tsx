import React from 'react';
import { ReactWidget } from '@jupyterlab/apputils';

export const JupyterAuthComponent = (data: any) => {
  const users = data.users.users
  return (
    <>
      {
        users.map((user: any) => 
          <div key={user.login}>
            <a href={`https://github.com/${user.login}`} target="_blank">
              <img src={user.avatar_url} style={{width: '100px'}}/>
              <div>{user.name}</div>
              <div className='jp-Auth-username'>@{user.login}</div>
              {user.bio && <div className='jp-Auth-bio'>Bio: {user.bio}</div>}
            </a>
            <hr/>
          </div> 
        )       
      }
    </>
  );
};

/**
 * A Auth Lumino Widget that wraps a AuthComponent.
 */
class AuthWidget extends ReactWidget {
  private users: [] = [];

  /**
   * Constructs a new CounterWidget.
   */
  constructor() {
    super();
    this.addClass('jp-Auth-Widget');
  }

  render(): JSX.Element {
    return <JupyterAuthComponent users={this.users}/>;
  }

  setUsers(users: []) {
    this.users = users;
    this.update();
  }

}

export default AuthWidget;
