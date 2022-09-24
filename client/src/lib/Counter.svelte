<script>
  let count = 0
  const increment = () => {
    count += 1
  }
</script>

<button class="bg-red-400 rounded-md p-5 text-3xl w-64" on:click={increment}>
  count is {count}
</button>
