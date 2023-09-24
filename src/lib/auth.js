import Cookies from 'js-cookie';

/**
 * Takes a username and unhashed password and attempts to verify the hashed password matches with the one in the server.
 * Returns a JWT for the client to use for their session.
 * @param {string} user_name the user's username
 * @param {string} password (unhashed) the user's password
 * @returns a JWT (json web token) for the (approved) client
 */
export async function loginUser(user_name, password) {

  const response = await fetch('/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ user_name, password })
  });
  
  if(response.ok) {
    const data = await response.json();
    Cookies.set('jwt', data.jwt);
    return data.jwt;
  } else throw new Error('failed to login');
}