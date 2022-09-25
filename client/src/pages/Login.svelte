<script>
	import { onMount } from "svelte";
	import axios from "axios";
	import { replace } from "svelte-spa-router";

	let login_checked = false;

	onMount(() => {
		axios.get("/api/logged_in")
			.then(res => {
				replace("/");
			})
			.catch(err => {
				login_checked = true;
			});
	});
</script>

{#if login_checked}

<h1>Login</h1>

<form method="post" action="/api/login">
	<input name="password" type="password">
	<button type="submit">
		Login
	</button>
</form>

{/if}