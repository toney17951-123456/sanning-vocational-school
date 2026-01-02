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

    <section class="courses-preview">
      <div class="container">
        <h2>热门课程</h2>
        <div class="courses-grid">
          <el-card v-for="course in courses" :key="course.id" class="course-card">
            <template #header>
              <div class="card-header">
                <h3>{{ course.name }}</h3>
              </div>
            </template>
            <div class="course-content">
              <p>{{ course.description }}</p>
              <div class="course-info">
                <span class="duration">{{ course.duration }}</span>
                <span class="price">¥{{ course.price }}</span>
              </div>
              <el-button type="primary" @click="$router.push(`/apply/${course.id}`)">立即报名</el-button>
            </div>
          </el-card>
        </div>
        <div class="view-all">
          <el-button type="default" @click="$router.push('/courses')">查看全部课程</el-button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { StarFilled, UserFilled, Document, Location } from '@element-plus/icons-vue'

// 模拟课程数据
const courses = ref([
  {
    id: 1,
    name: 'Office三剑客',
    description: '包括word、excel、ppt必备核心技能，实现高效办公。',
    duration: '10天',
    price: 3999
  },
  {
    id: 2,
    name: 'AI应用助力高效办公',
    description: '学习AI应用，提升办公效率，实现智能办公。',
    duration: '2天',
    price: 1399
  },
  {
    id: 3,
    name: 'TTT：培训师培训',
    description: '培训师培训，提升专、兼职讲师培训技能，实现突破自我，真正成为一位接受市场考研的专业培训讲师。',
    duration: '4天',
    price: 1999
  }
])
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

.courses-preview {
  padding: 3rem 0;
  background-color: #f5f5f5;
}

.courses-preview h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

.courses-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.course-card {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.course-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.course-content p {
  margin-bottom: 1rem;
  flex: 1;
}

.course-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.duration {
  color: #666;
}

.price {
  font-weight: bold;
  color: #e6a23c;
}

.view-all {
  text-align: center;
}
</style>