<template>
  <div id="app">
    <div class="nav">
      <h4>Soccer League Management</h4>
      <router-link to="/index">Ligas</router-link>
      
    </div>
    <div class="content">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  display: flex;
}
.nav {
  flex: 20%;
  height: 100vh;
  background-color: #363740;
  color: #A4A6B3;
}
h4 {
  margin: 10px 0 0 0;
}
.content {
  flex: 80%;
}
</style>
