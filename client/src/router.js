import Vue from 'vue';
// vue add router
import VueRouter from 'vue-router';
import Ping from './components/Ping.vue'

Vue.use(VueRouter);

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/ping',
            name: 'Ping',
            component: Ping,
        }
    ],
});