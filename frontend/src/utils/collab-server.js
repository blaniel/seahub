import io from 'socket.io-client';
import { name, username, contactEmail, seafileCollabServer } from './constants';

const socket = io(seafileCollabServer);

class CollabServer {

  watchRepo(repoID, fn) {
    socket.emit('repo_update', {
      request: 'watch_update',
      repo_id: repoID,
      user: {
        name: name,
        username: username,
        contact_email: contactEmail,
      },
    });

    socket.on('repo_update', fn)
  }

  unwatchRepo(repoID) {
    socket.emit('repo_update', {
      request: 'unwatch_update',
      repo_id: repoID,
      user: {
        name: name,
        username: username,
        contact_email: contactEmail,
      },
    });
  }
}

const collabServer = new CollabServer();

export default collabServer;