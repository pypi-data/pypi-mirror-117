import React, { useState, useEffect } from 'react';
import { styled } from '@material-ui/core/styles';
import Avatar from '@material-ui/core/Avatar';
import AvatarGroup from '@material-ui/core/AvatarGroup';
import Badge from '@material-ui/core/Badge';
import Stack from '@material-ui/core/Stack';
import { requestAPI } from '../handler';

const StyledBadge = styled(Badge)(({ theme }) => ({
  '& .MuiBadge-badge': {
    backgroundColor: '#44b700',
    color: '#44b700',
    boxShadow: `0 0 0 2px ${theme.palette.background.paper}`,
    '&::after': {
      position: 'absolute',
      top: 0,
      left: 0,
      width: '100%',
      height: '100%',
      borderRadius: '50%',
      animation: 'ripple 1.2s infinite ease-in-out',
      border: '1px solid currentColor',
      content: '""',
    },
  },
  '@keyframes ripple': {
    '0%': {
      transform: 'scale(.8)',
      opacity: 1,
    },
    '100%': {
      transform: 'scale(2.4)',
      opacity: 0,
    },
  },
}));

const getUsers = () => {
  return requestAPI<any>('users')
    .then(data => {
//      console.log('Response from the jupytery_auth server API', data);
      return data;
    })
    .catch(reason => {
      console.log('The jupytery_auth server API appears to be failing', reason);
    });
}

const JupyterUsers = () => {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    const refreshUsers = () => getUsers().then((data) => {
      setUsers(data.users);
    });
    void refreshUsers();
    setInterval(async () => {
      void refreshUsers();
    }, 5000);
  }, [])
  return (
    <Stack direction="row" spacing={2}>
      <AvatarGroup max={4}>
        {
          users.map((user: any) =>
            <StyledBadge
              overlap="circular"
              anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
              variant="dot"
            >
              <Avatar alt={user.login} src={user.avatar_url} />
            </StyledBadge>
            /*
              {user.name}
              {user.login}
              {user.bio && {user.bio}}
            */
          )
        }
      </AvatarGroup>
    </Stack>
  );
}

export default JupyterUsers;
