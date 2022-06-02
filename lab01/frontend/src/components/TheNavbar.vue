<template>
  <div class="w-full shadow flex justify-between px-3 py-4">
      <span class="font-bold text-md px-3 text-neutral-900">TODOApp</span>
      <div class="flex justify-between gap-x-4 px-3 text-neutral-900">
          <router-link :to="{name: 'Register'}">Register a new account</router-link>
          <router-link :to="{name: 'Login'}">Switch account</router-link>
      </div>

  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>