<template>
  <img alt="Vue logo" src="./assets/intuitive-care-squareLogo-1719739952136.webp">
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <SearchApp /> <!-- Aqui estamos utilizando o componente -->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import SearchApp from './components/SearchApp.vue'

export default {
  name: 'App',
  components: {
    SearchApp,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
