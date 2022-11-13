<template>
  <div id="app">
    <div class="nav">
      <h4>Soccer League Management</h4>

      <div class="nav-link">
        <router-link class="link" to="/index">Ligas</router-link>
        <router-link class="link" to="/referees">Arbitros</router-link>
      </div>
      
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
    flex: 15%;
    height: 100vh;
    background-color: #363740;
    color: #A4A6B3;
  }
  .nav-link {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
  }
  .link {
    display: block;
    color: #A4A6B3; 
    text-align: left;
    margin: 30px 0 0 15px;
  }
  h4 {
    box-sizing: border-box;
    padding: 0;
    margin: 10px 0 0 0;
  }
  .content {
    flex: 85%;
  }
</style>
