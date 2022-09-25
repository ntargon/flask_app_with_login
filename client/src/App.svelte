<script lang='typescript'>
  import Router from 'svelte-spa-router'
  import Header from './lib/Header.svelte';
  import { routes } from './router'
  import { push } from 'svelte-spa-router';
  import { onMount } from "svelte";
  import axios from 'axios';

  let logged_in_checked = false;

  const loggedIn = () => {
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

  onMount(async () => {
      // ログインしていなければ、loginページに飛ばす
      let res = await loggedIn();
      if (!res) {
          push('/login');
      }
      logged_in_checked = true;
  });
</script>


<main>
  <Header />
  {#if logged_in_checked}
  <Router {routes} />
  {/if}
</main>

<style>
</style>
