<template>
  <div class="news-container">
    <div class="container">
      <h2>新闻中心</h2>
      <p class="news-intro">了解学校最新动态和行业资讯</p>

      <div class="news-list">
        <el-card v-for="news in newsList" :key="news.id" class="news-card">
          <div class="news-content">
            <div class="news-image">
              <el-image
                :src="news.cover_image || 'https://picsum.photos/400/300?random=' + news.id"
                fit="cover"
                :preview-src-list="[news.cover_image || 'https://picsum.photos/400/300?random=' + news.id]"
              >
                <template #error>
                  <div class="image-slot">
                    <el-icon><PictureFilled /></el-icon>
                  </div>
                </template>
              </el-image>
            </div>
            <div class="news-info">
              <h3 class="news-title">{{ news.title }}</h3>
              <p class="news-excerpt">{{ news.content }}</p>
              <div class="news-meta">
                <span class="news-author">{{ news.author }}</span>
                <span class="news-date">{{ news.created_at }}</span>
              </div>
              <el-button type="primary" size="small" @click="showNewsDetail(news)">
                阅读全文
              </el-button>
            </div>
          </div>
        </el-card>
      </div>

      <div class="pagination-container">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="100"
          :page-size="10"
          @current-change="handleCurrentChange"
        />
      </div>
    </div>

    <!-- 新闻详情对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="selectedNews.title"
      width="70%"
      center
    >
      <div v-if="selectedNews" class="news-detail">
        <div class="detail-header">
          <span class="detail-author">{{ selectedNews.author }}</span>
          <span class="detail-date">{{ selectedNews.created_at }}</span>
        </div>
        <div class="detail-image" v-if="selectedNews.cover_image">
          <el-image
            :src="selectedNews.cover_image"
            fit="cover"
            :preview-src-list="[selectedNews.cover_image]"
          >
            <template #error>
              <div class="image-slot">
                <el-icon><PictureFilled /></el-icon>
              </div>
            </template>
          </el-image>
        </div>
        <div class="detail-content">
          <p>{{ selectedNews.content }}</p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
          <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
      </div>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">关闭</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { PictureFilled } from '@element-plus/icons-vue'

// 模拟新闻数据
const newsList = ref([
  {
    id: 1,
    title: '三宁职校2025年春季招生开始',
    content: '三宁职校2025年春季招生现已开始，欢迎广大学生报名咨询。本次招生开设多个热门专业，包括Web前端开发、Python后端开发、UI/UX设计等。',
    author: '管理员',
    cover_image: 'https://picsum.photos/400/300?random=1',
    created_at: '2025-01-15 10:00:00'
  },
  {
    id: 2,
    title: '学校与多家企业签订校企合作协议',
    content: '近日，我校与多家知名企业签订了校企合作协议，将为学生提供更多实习和就业机会。',
    author: '管理员',
    cover_image: 'https://picsum.photos/400/300?random=2',
    created_at: '2025-01-10 14:30:00'
  },
  {
    id: 3,
    title: '我校教师在全国技能大赛中获奖',
    content: '我校张老师在2024年全国职业技能大赛中获得一等奖，为学校赢得了荣誉。',
    author: '管理员',
    cover_image: 'https://picsum.photos/400/300?random=3',
    created_at: '2025-01-05 09:15:00'
  },
  {
    id: 4,
    title: '2024年秋季毕业典礼圆满结束',
    content: '2024年秋季毕业典礼于12月30日圆满结束，共有200名学生顺利毕业。',
    author: '管理员',
    cover_image: 'https://picsum.photos/400/300?random=4',
    created_at: '2024-12-31 16:45:00'
  },
  {
    id: 5,
    title: '学校新增多个实训实验室',
    content: '为了提高学生的实践能力，学校新增了多个实训实验室，包括Web开发实验室、UI设计实验室等。',
    author: '管理员',
    cover_image: 'https://picsum.photos/400/300?random=5',
    created_at: '2024-12-20 11:20:00'
  }
])

// 新闻详情对话框
const dialogVisible = ref(false)
const selectedNews = ref(null)

const showNewsDetail = (news) => {
  selectedNews.value = news
  dialogVisible.value = true
}

const handleCurrentChange = (val) => {
  console.log(`当前页: ${val}`)
  // 这里可以添加分页逻辑
}
</script>

<style scoped>
.news-container {
  padding: 2rem 0;
  background-color: #fff;
}

.news-intro {
  text-align: center;
  margin-bottom: 3rem;
  color: #666;
  font-size: 1.1rem;
}

.news-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-bottom: 2rem;
}

.news-card {
  transition: transform 0.3s, box-shadow 0.3s;
}

.news-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.news-content {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
  flex-wrap: wrap;
}

.news-image {
  flex: 0 0 300px;
  border-radius: 8px;
  overflow: hidden;
  height: 200px;
}

.news-image :deep(.el-image) {
  width: 100%;
  height: 100%;
}

.news-info {
  flex: 1;
  min-width: 300px;
}

.news-title {
  margin: 0 0 1rem 0;
  font-size: 1.3rem;
  color: #2c3e50;
  cursor: pointer;
  transition: color 0.3s;
}

.news-title:hover {
  color: #409eff;
}

.news-excerpt {
  margin-bottom: 1rem;
  line-height: 1.8;
  color: #666;
}

.news-meta {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
  color: #999;
  font-size: 0.9rem;
}

.pagination-container {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}

.news-detail {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  color: #999;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.detail-image {
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 2rem;
}

.detail-image :deep(.el-image) {
  width: 100%;
  height: auto;
}

.detail-content {
  line-height: 2;
  color: #333;
}

.detail-content p {
  margin-bottom: 1.5rem;
}

.image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-color: #f5f5f5;
  color: #909399;
  font-size: 2rem;
}
</style>