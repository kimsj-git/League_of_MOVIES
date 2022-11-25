<template style="background-color: white">
  <div>
    <h1 style="color: white">Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username" style="color: white">username : </label>
      <input type="text" id="username" v-model="username" /><br />

      <label for="password1" style="color: white"> password : </label>
      <input type="password" id="password1" v-model="password1" /><br />

      <label for="password2" style="color: white"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2" />
      
      <input type="submit" style="color: white" value="SignUp" />
    </form>
  </div>
</template>

  <script>
export default {
  name: "SignUpView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signUp() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      };

      this.$store.dispatch("signUp", payload);
    },
  },
};
</script>

<style>
input, select, textarea{
    color: white;
    border-color: white;
}
</style>