<template>
  <header class="header">
    <div class="logo">
      <img src="/path/to/logo.png" alt="Logo" />
    </div>
    <div class="search-box">
      <input type="text" placeholder="Search..." />
    </div>
    <nav class="nav-items">
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background-color: #f8f8f8;
  border-bottom: 1px solid #eaeaea;
}

.logo img {
  height: 50px;
}

.search-box input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.nav-items ul {
  display: flex;
  list-style: none;
  padding: 0;
}

.nav-items li {
  margin: 0 1rem;
}

.nav-items a {
  text-decoration: none;
  color: #333;
}

.nav-items a:hover {
  text-decoration: underline;
}
</style>