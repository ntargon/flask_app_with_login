import {wrap} from 'svelte-spa-router/wrap'
import axios from 'axios'
import Page1 from '../pages/Page1.svelte'
import Page2 from '../pages/Page2.svelte'
import Login from '../pages/Login.svelte'

const loggedIn = (): Promise<boolean> => {
  return new Promise((resolve, reject) => {
    axios.get('/api/logged_in')
      .then(res => {
        resolve(true);
      })
      .catch(err => {
        resolve(false);
      });
  });
};

const loginRequired = (component) => {
  return wrap({
    asyncComponent: () => component,
    conditions: [
      async (detail) => {
        const res = await loggedIn();
        return res;
      }
    ]
  });
}

export const routes = {
  '/': loginRequired(Page1),
  '/page2': loginRequired(Page2),
  '/login': Login
}