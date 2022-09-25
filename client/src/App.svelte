<script lang='typescript'>
  import Router, { push, replace } from 'svelte-spa-router'
  import Header from './lib/Header.svelte';
  import { routes } from './router'

  const conditionsFailed = (event) => {
    replace("/login");
  }
</script>


<main>
  <Header />
  <Router
    {routes}
    on:conditionsFailed={conditionsFailed}
  />
</main>

<style>
</style>
