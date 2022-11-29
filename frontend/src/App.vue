<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand class="nav-title" href="#"><router-link class="logo" to="/"><img class="nav-logo" src="./assets/logo_app.png" alt="logo"></router-link></b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#"><router-link class="link" to="/leagues">Ligas</router-link></b-nav-item>
          <b-nav-item href="#"><router-link class="link" to="/referees">Arbitros</router-link></b-nav-item>
          <b-nav-item href="#"><router-link class="link" to="/managers">Representantes de equipo</router-link></b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>

    </b-navbar>
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
    flex-direction: column;
  }
  .nav-title {
    font-size: small;
  }
  .nav-link {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
  }
  .nav-logo {
    width: 60px;
    height: 60px;
    display: inline-block;
  }
  .logo {
    color: #2c3e50;
  }
  .link {
    display: block;
    color: white; 
    text-align: left;
    padding: 15px;
  }
  .link:hover {
    text-decoration: none;
    background-color: #9FA2B4;
    color: white;
  }
  h4 {
    box-sizing: border-box;
    padding: 0;
    margin: 10px 0 0 0;
  }
</style>
