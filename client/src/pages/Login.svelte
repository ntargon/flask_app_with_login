<script>
	import { onMount } from "svelte";
	import axios from "axios";
	import { replace } from "svelte-spa-router";

	let login_checked = false;
	let password;

	const login = () => {
		axios.post(
			"/api/login",
			{password}
		).then(res => {
			replace("/")
		}).catch(err => {
		})
	};

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

<form on:submit|preventDefault={login}>
	<input bind:value={password} type="password">
	<button type="submit">
		Login
	</button>
</form>

{/if}