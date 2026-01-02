<template>
  <div class="app-container">
    <!-- 导航栏 -->
    <header class="app-header">
      <div class="container">
        <div class="logo">
          <h1>三宁职校</h1>
        </div>
        <nav>
          <router-link to="/">首页</router-link>
          <router-link to="/about">学校简介</router-link>
          <router-link to="/teachers">师资介绍</router-link>
          <router-link to="/courses">业务项目</router-link>
        </nav>
      </div>
    </header>
    
    <!-- 主要内容 -->
    <main class="app-main">
      <router-view />
    </main>
    
    <!-- 页脚 -->
    <footer class="app-footer">
      <div class="container">
        <p>&copy; 2026 三宁职校. 保留所有权利.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
// App组件逻辑
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  background-color: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 1rem 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo h1 {
  margin: 0;
  color: #409eff;
  font-size: 1.8rem;
}

nav {
  display: flex;
  gap: 2rem;
  align-items: center;
}

nav a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  transition: color 0.3s;
}

nav a:hover {
  color: #409eff;
}

.app-main {
  flex: 1;
  padding: 2rem 0;
  background-color: #f5f5f5;
}

.app-footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
  margin-top: auto;
}
</style>