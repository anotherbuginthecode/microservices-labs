import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'
import interceptor from './api/interceptors'

interceptor()

createApp(App).use(router).mount('#app')
