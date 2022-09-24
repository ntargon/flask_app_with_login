<script lang='typescript'>
  import Router from 'svelte-spa-router'
  import { routes } from './router'
  import { push } from 'svelte-spa-router';
  import { onMount } from "svelte";
  import axios from 'axios';

  let logged_in_checked = false;

  const loggedIn = () => {
    return new Promise((resolve, reject) => {
      axios.get('/logged_in')
        .then(res => {
          resolve(true);
        })
        .catch(err => {
          resolve(false);
        });
    });
  };

  onMount(async () => {
      // ログインしていなければ、loginページに飛ばす
      let res = await loggedIn();
      if (!res) {
          push('/login');
      }
      logged_in_checked = true;
  });
</script>

{#if logged_in_checked}
<main>
  <nav><a href="/logout">logout</a></nav>
  <Router {routes} />
</main>
{/if}

<style>
</style>
