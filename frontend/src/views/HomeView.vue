<template>
  <div class="home-container">
    <el-carousel height="400px" :interval="3000" arrow="hover">
      <el-carousel-item>
        <div class="carousel-item" style="background-color: #409eff;">
          <h2>欢迎来到三宁职校</h2>
          <p>培养专业技能，成就美好未来</p>
        </div>
      </el-carousel-item>
      <el-carousel-item>
        <div class="carousel-item" style="background-color: #67c23a;">
          <h2>专业师资团队</h2>
          <p>行业专家亲自授课，理论实践相结合</p>
        </div>
      </el-carousel-item>
      <el-carousel-item>
        <div class="carousel-item" style="background-color: #e6a23c;">
          <h2>多样化课程</h2>
          <p>满足不同学员的学习需求</p>
        </div>
      </el-carousel-item>
    </el-carousel>

    <section class="features">
      <div class="container">
        <h2>我们的优势</h2>
        <div class="features-grid">
          <div class="feature-item">
            <el-icon class="feature-icon"><StarFilled /></el-icon>
            <h3>专业认证</h3>
            <p>国家认可的职业技能培训资质</p>
          </div>
          <div class="feature-item">
            <el-icon class="feature-icon"><UserFilled /></el-icon>
            <h3>名师团队</h3>
            <p>行业资深专家和技术能手</p>
          </div>
          <div class="feature-item">
            <el-icon class="feature-icon"><Document /></el-icon>
            <h3>实战教学</h3>
            <p>理论结合实践，注重技能培养</p>
          </div>
          <div class="feature-item">
            <el-icon class="feature-icon"><Location /></el-icon>
            <h3>技能提升</h3>
            <p>结合成人学习特点，注重技能应用提升</p>
          </div>
        </div>
      </div>
    </section>


  </div>
</template>

<script setup>
import { ref } from 'vue'
import { StarFilled, UserFilled, Document, Location } from '@element-plus/icons-vue'
</script>

<style scoped>
.home-container {
  width: 100%;
}

.carousel-item {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  color: white;
  text-align: center;
}

.carousel-item h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.carousel-item p {
  font-size: 1.2rem;
}

.features {
  padding: 3rem 0;
  background-color: white;
}

.features h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.feature-item {
  text-align: center;
  padding: 2rem;
  background-color: #f9f9f9;
  border-radius: 8px;
  transition: transform 0.3s;
}

.feature-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 2.5rem;
  color: #409eff;
  margin-bottom: 1rem;
}
</style>