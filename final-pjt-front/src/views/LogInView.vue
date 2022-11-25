<template>
    <div>
      <h1 style="color: white">LogIn Page</h1>
      <form @submit.prevent="logIn">
        <label for="username" style="color: white">username : </label>
        <input type="text" id="username" v-model="username"><br>
  
        <label for="password" style="color: white"> password : </label>
        <input type="password" id="password" v-model="password"><br>
  
        <input type="submit" style="color: white" value="logIn">
      </form>
      <br>
      <p>아직 회원이 아니신가요?</p>
      <p>⬇⬇⬇⬇⬇⬇⬇⬇⬇</p>
      <router-link to="/signup">❤Ѽ즉ㅅ17ㅏ입❤✧</router-link>
      <p>➼ヌㅣ금 7ㅏ입ㅅ1 ㅇㅏㅇ1ㄷ1♂ 丨0❤0% 증정!❚!✯</p>
    </div>
</template>
  
  <script>
  export default {
    name: 'LogInView',
    data() {
      return {
        username: null,
        password: null,
      }
    },
    methods: {
      logIn() {
        const username = this.username
        const password = this.password
  
        const payload = {
          username: username,
          password: password,
        }
        this.$store.dispatch('logIn', payload)
      }
    }
  }
  </script>