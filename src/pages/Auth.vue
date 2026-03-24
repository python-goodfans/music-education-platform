<template>
  <div class="auth-container">
    <h1>Authentication</h1>
    <div class="forms">
      <form @submit.prevent="handleLogin">
        <h2>Login</h2>
        <input type="text" v-model="loginEmail" placeholder="Email" required />
        <input type="password" v-model="loginPassword" placeholder="Password" required />
        <button type="submit">Login</button>
      </form>
      <form @submit.prevent="handleRegistration">
        <h2>Register</h2>
        <input type="text" v-model="registerName" placeholder="Name" required />
        <input type="text" v-model="registerEmail" placeholder="Email" required />
        <input type="password" v-model="registerPassword" placeholder="Password" required />
        <button type="submit">Register</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginEmail: '',
      loginPassword: '',
      registerName: '',
      registerEmail: '',
      registerPassword: '',
    };
  },
  methods: {
    handleLogin() {
      // Handle login logic here
      console.log('Logging in with', this.loginEmail);
    },
    handleRegistration() {
      // Handle registration logic here
      console.log('Registering', this.registerName);
    },
  },
};
</script>

<style scoped>
.auth-container {
  width: 300px;
  margin: auto;
} 
.forms {
  display: flex;
  flex-direction: column;
}
form {
  margin-bottom: 20px;
}
input {
  margin-bottom: 10px;
  padding: 10px;
  width: 100%;
  box-sizing: border-box;
}
button {
  padding: 10px;
  width: 100%;
}
</style>