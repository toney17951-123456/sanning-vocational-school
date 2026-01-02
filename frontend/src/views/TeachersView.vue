<template>
  <div class="teachers-container">
    <div class="container">
      <h2>师资介绍</h2>
      <p class="teachers-intro">我们拥有一支专业的师资团队，由行业专家和资深教师组成，致力于为学员提供优质的教育服务。</p>

      <div class="teachers-grid">
        <el-card v-for="teacher in teachers" :key="teacher.id" class="teacher-card">
          <template #header>
            <div class="teacher-header">
              <div class="teacher-avatar">
                <el-image
                  :src="(teacher.avatar ? BASE_URL + teacher.avatar.slice(1) : 'https://picsum.photos/200/200?random=' + teacher.id)"
                  fit="cover"
                  round
                  :preview-src-list="[teacher.avatar ? BASE_URL + teacher.avatar.slice(1) : 'https://picsum.photos/200/200?random=' + teacher.id]"
                >
                  <template #error>
                    <div class="avatar-slot">
                      <el-icon><UserFilled /></el-icon>
                    </div>
                  </template>
                </el-image>
              </div>
              <div class="teacher-info">
                <h3>{{ teacher.name }}</h3>
                <p class="teacher-title">{{ teacher.title }}</p>
              </div>
            </div>
          </template>
          <div class="teacher-content">
            <p class="teacher-bio">{{ teacher.bio }}</p>
            <div class="teacher-courses">
              <h4>擅长课程</h4>
              <div v-if="teacher.courses.length > 0" class="courses-list">
                <div v-for="course in teacher.courses" :key="course.id" class="course-item" @click="navigateToCourse(course)">
                  <span class="course-name">{{ course.name }}</span>
                  <span class="hover-tip">点击查看课程详情</span>
                </div>
              </div>
              <div v-else class="no-courses">
                暂无课程
              </div>
            </div>
          </div>
        </el-card>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { UserFilled } from '@element-plus/icons-vue'

const router = useRouter()
const BASE_URL = import.meta.env.BASE_URL

// 导航到课程详情
const navigateToCourse = (course) => {
  // 从课程名称中提取纯文本（去掉书名号）
  const courseName = course.name.replace(/《|》/g, '')
  router.push({ path: '/courses', query: { courseName } })
}

// 模拟师资数据
const teachers = ref([
  {
    id: 3,
    name: '陈老师',
    title: '国家注册安全工程师、高级人力资源管理师、法律职业资格',
    bio: '15年安全生产与法律培训经验，专注于企业安全法规解读与工伤预防实务，已为众多企业提供风险防控培训与咨询服务。擅长将复杂法条转化为实操要点，助力企业构建合规管理体系。',
    avatar: '/images/teacher-chenkaihong.png',
    courses: [
      { id: 12, name: '《习总书记关于安全生产重要论述与精神》' },
      { id: 13, name: '《安全生产法等安全生产法律法规解读》' },
      { id: 14, name: '《工伤保险和工伤预防政策解读》' },
      { id: 15, name: '《企业员工法律基础常识》' },
      { id: 16, name: '《维修钳工实训指导》' },
      { id: 17, name: '《劳动关系法律风险与处理》' }
    ]
  },
  {
    id: 8,
    name: '滕老师',
    title: '高级经济师、质量工程师',
    bio: '化工行业质量管理从业20年，专职人力资源管理研究与实践10年，擅长人力资源管理策划与企业管理培训。',
    avatar: '/images/teacher-tengaiping.jpg',
    courses: [
      { id: 29, name: '《企业文化建设》' },
      { id: 30, name: '《人力资源管理体系策划》' },
      { id: 31, name: '《绩效管理》' }
    ]
  },
  {
    id: 5,
    name: '许老师',
    title: '仪表维修工程师',
    bio: '深耕继续教育和职业培训十余年，具备“教育运营+技能评价”双轮驱动能力，主导学历教育与工匠认证体系融合；输出“三宁标准”并对外提供行业解决方案，探索从企业内训到市场化办学的跨越渠道。',
    avatar: '/images/teacher-xuzhijun.jpg',
    courses: [
      { id: 21, name: '《化工仪表自动化》' },
      { id: 22, name: '《职业技能等级认定体系建设》' },
      { id: 23, name: '《化工专业课程建设》' }
    ]
  },
  {
    id: 4,
    name: '刘老师',
    title: '注册安全工程师',
    bio: '具有多年化工安全生产教育培训经验，致力于增强员工安全意识和提升安全技能。',
    avatar: 'https://picsum.photos/200/200?random=4',
    courses: [
      { id: 18, name: '《化工企业员工安全教育培训》' },
      { id: 19, name: '《化工检维修人员作业安全》' },
      { id: 20, name: '《事故应急处置实操实训》' }
    ]
  },
  {
    id: 1,
    name: '蔡老师',
    title: '高级企业培训师',
    bio: '15年企业培训师经验，专注于企业级应用培训和解决方案设计，已服务于多个大、中型企业客户,一直致力于“个人效能提升”领域研究与实践。',
    avatar: '/images/teacher-caitiebing.png',
    courses: [
      { id: 1, name: '《TTT：培训师培训》' },
      { id: 2, name: '《AI应用助力高效办公》' },
      { id: 3, name: '《工匠精神》' },
      { id: 4, name: '《Office三剑客》' },
      { id: 5, name: '《数字化能力提升》' },
      { id: 6, name: '《Excel实用技能》' },
      { id: 32, name: '《飞书高效应用》' },
      { id: 7, name: '《BI看板制作》' }
    ]
  },
  {
    id: 2,
    name: '陈老师',
    title: '高级企业培训师',
    bio: '12年公共课授课经验，专注于职场礼仪、职业素养、高效沟通、深度逻辑思维等领域课程研究。当下，正致力于数字化能力提升及AI应用领域创新与课程开发。陈老师人美心善，擅长讲解复杂概念和深度晦涩问题，使学生容易理解和掌握。',
    avatar: '/images/teacher-chenying.jpg',
    courses: [
      { id: 8, name: '《职场礼仪》' },
      { id: 9, name: '《职业素养》' },
      { id: 10, name: '《高效沟通》' },
      { id: 11, name: '《逻辑思维》' }
    ]
  },
  {
    id: 6,
    name: '熊老师',
    title: '化工单元操作高级工',
    bio: '负责危化工艺理论与实训教学，通过实训提升学员实操能力，为化工企业培养安全专业人才。',
    avatar: '/images/teacher-xiongchenyang.jpg',
    courses: [
      { id: 24, name: '《硝化工艺》' },
      { id: 25, name: '《氧化工艺》' },
      { id: 26, name: '《氯化工艺》' }
    ]
  },
  {
    id: 7,
    name: '李老师',
    title: '注册安全工程师',
    bio: '持有多项专业资质：中级注册安全工程师、高中化学教师资格证、仪表高级工及中级消防设施操作员。职业生涯始于湖北三宁公司，先后在尿素厂电仪车间与物流公司检修车间从事一线技术工作，积累了扎实的现场实践经验。',
    avatar: '/images/teacher-lichuang.png',
    courses: [
      { id: 27, name: '《消防法律法规及通用规范解读》' },
      { id: 28, name: '《电工识图》' }
    ]
  }
])
</script>

<style scoped>
.teachers-container {
  padding: 2rem 0;
  background-color: #fff;
}

.teachers-intro {
  text-align: center;
  margin-bottom: 3rem;
  color: #666;
  font-size: 1.1rem;
}

.teachers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.teacher-card {
  height: 100%;
  transition: transform 0.3s, box-shadow 0.3s;
}

.teacher-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.teacher-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 0;
}

.teacher-avatar {
  width: 100px;
  height: 100px;
  flex-shrink: 0;
}

.teacher-avatar :deep(.el-image) {
  width: 100%;
  height: 100%;
}

.teacher-info {
  flex: 1;
}

.teacher-info h3 {
  margin: 0;
  font-size: 1.3rem;
  color: #2c3e50;
}

.teacher-title {
  margin: 0.5rem 0 0 0;
  color: #409eff;
  font-size: 1rem;
}

.teacher-content {
  padding: 1rem 0;
}

.teacher-bio {
  margin-bottom: 1.5rem;
  line-height: 1.8;
  color: #666;
}

.teacher-courses h4 {
  margin-bottom: 1rem;
  font-size: 1rem;
  color: #333;
}

.courses-list {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.course-item {
  position: relative;
  padding: 0.3rem 0;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
}

.course-name {
  font-size: 1rem;
  font-weight: bold;
  color: #2c3e50;
  transition: color 0.3s ease;
}

.course-item:hover .course-name {
  color: #409eff;
}

.hover-tip {
  position: absolute;
  left: 100%;
  margin-left: 10px;
  padding: 0.4rem 0.8rem;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  font-size: 0.85rem;
  border-radius: 4px;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 100;
}

.hover-tip::before {
  content: '';
  position: absolute;
  right: 100%;
  top: 50%;
  transform: translateY(-50%);
  border: 5px solid transparent;
  border-right-color: rgba(0, 0, 0, 0.8);
}

.course-item:hover .hover-tip {
  opacity: 1;
  visibility: visible;
}

.no-courses {
  padding: 1rem 0;
  color: #909399;
  font-size: 0.9rem;
}

.avatar-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: #f5f5f5;
  color: #909399;
  font-size: 2rem;
}
</style>