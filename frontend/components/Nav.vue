<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="/">
          <img src="~/assets/images/logo.png" alt="logo" class="image">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
         <b-nav-item to="/">หน้าหลัก</b-nav-item>
        </b-navbar-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
        <div v-if="isAuthenticated==true">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              {{loggedInUser.email}}
            </template>
            <b-dropdown-item to="/profile/">โปรไฟล์</b-dropdown-item>
            <b-dropdown-item > <span @click="logout()">ลงชื่อออก</span></b-dropdown-item>
          </b-nav-item-dropdown>
        </div>
        <div v-else>
            <b-nav-item to="/login/">ลงชื่อเข้าใช้</b-nav-item>
        </div>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
    middleware: 'auth',
    computed: {
        ...mapGetters(['isAuthenticated', 'loggedInUser']),
    },
    methods: {
        logout(){
            this.$auth.logout()
        }
    }
};
</script>

<style  scoped>
.image{
    height: 2.3em;
}
 .navbar.navbar-light.bg-light{
    background-color: #f1f0f0!important;
    box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.2), 0 1px 10px 0 rgba(0, 0, 0, 0.19);
 }
</style>