<template>
  <div class="h-screen w-full flex justify-center items-center">
      <div class="w-1/2">
        <h1 class="text-center text-2xl font-bold text-neutral-900">Login</h1>
        
        <!-- login form -->
        <div class="flex justify-center mt-10">
            <label for="email-address" class="sr-only">Email address</label>
            <input v-model="email" id="email-address" name="email" type="email" autocomplete="email" required class="appearance-none rounded-none relative block w-1/2 px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none sm:text-sm" placeholder="Email address">
        </div>
        <div class="flex justify-center">
            <label for="password" class="sr-only">Password</label>
            <input v-model="password" id="password" name="password" type="password" autocomplete="current-password" required class="appearance-none rounded-none relative block w-1/2 px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none sm:text-sm" placeholder="Password">
        </div>

        <div class="flex justify-center mt-5">
            <button 
                @click="handleLogin"
                class="w-1/2 bg-green-400 text-white uppercase py-2 rounded hover:bg-green-500">
                Login
            </button>
        </div>

        <div class="text-center text-neutral-500 mt-5 opacity-60 hover:opacity-100">
            <router-link :to="{name: 'Register'}">Create a new Account</router-link>
        </div>


      </div>
  </div>
</template>

<script>
import { AUTH_API } from '@/api/auth/http-common.js'

export default {

    data () {
        return{
            email: '',
            password: ''
        }
    },
    methods: {

        handleLogin: function(){
            AUTH_API.post('/api/v1/auth/token/', {
                'email': this.email,
                'password': this.password
            })
            .then((res) => {
                sessionStorage.setItem('jwt', res.data.access)
                this.$router.push({name: 'Home'});
            })

        }

    }

}
</script>

<style>

</style>