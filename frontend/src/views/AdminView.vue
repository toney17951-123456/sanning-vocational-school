<template>
  <div class="admin-container">
    <!-- 登录页面 -->
    <div v-if="!isLoggedIn" class="login-container">
      <el-card class="login-card">
        <h2 class="login-title">管理员登录</h2>
        <el-form
          :model="loginForm"
          :rules="loginRules"
          ref="loginFormRef"
          label-width="80px"
          class="login-form"
        >
          <el-form-item label="用户名" prop="username">
            <el-input v-model="loginForm.username" placeholder="请输入用户名" />
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input
              v-model="loginForm.password"
              type="password"
              placeholder="请输入密码"
              show-password
            />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="login" :loading="loginLoading" class="login-btn">
              登录
            </el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </div>

    <!-- 后台管理页面 -->
    <div v-else class="admin-main">
      <!-- 侧边导航 -->
      <aside class="admin-sidebar">
        <div class="sidebar-header">
          <h3>三宁职校后台</h3>
        </div>
        <el-menu
          :default-active="activeMenu"
          class="el-menu-vertical-demo"
          @select="handleMenuSelect"
        >
          <el-menu-item index="applications">
            <el-icon><List /></el-icon>
            <span>报名管理</span>
          </el-menu-item>
          <el-menu-item index="news">
            <el-icon><Document /></el-icon>
            <span>新闻管理</span>
          </el-menu-item>
          <el-menu-item index="teachers">
            <el-icon><User /></el-icon>
            <span>师资管理</span>
          </el-menu-item>
          <el-menu-item index="courses">
            <el-icon><Collection /></el-icon>
            <span>课程管理</span>
          </el-menu-item>
          <el-menu-item index="users">
            <el-icon><Setting /></el-icon>
            <span>用户管理</span>
          </el-menu-item>
        </el-menu>
        <div class="sidebar-footer">
          <el-button type="text" @click="logout">
            <el-icon><SwitchButton /></el-icon>
            退出登录
          </el-button>
        </div>
      </aside>

      <!-- 主内容区域 -->
      <main class="admin-content">
        <header class="content-header">
          <h2>{{ getMenuTitle(activeMenu) }}</h2>
          <div class="user-info">
            <span>{{ currentUser }}</span>
          </div>
        </header>

        <!-- 报名管理 -->
        <div v-if="activeMenu === 'applications'" class="content-body">
          <el-card>
            <template #header>
              <div class="card-header">
                <span>报名数据列表</span>
                <el-button type="primary" size="small">
                  <el-icon><Download /></el-icon>
                  导出数据
                </el-button>
              </div>
            </template>
            <el-table :data="applications" style="width: 100%" stripe>
              <el-table-column prop="id" label="ID" width="80" />
              <el-table-column prop="name" label="姓名" />
              <el-table-column prop="phone" label="手机号码" />
              <el-table-column prop="email" label="电子邮箱" />
              <el-table-column prop="course" label="课程" />
              <el-table-column prop="status" label="状态">
                <template #default="scope">
                  <el-tag :type="scope.row.status === 'pending' ? 'warning' : scope.row.status === 'paid' ? 'success' : 'info'">
                    {{ scope.row.status }}
                  </el-tag>
                </template>
              </el-table-column>
              <el-table-column prop="payment_status" label="支付状态">
                <template #default="scope">
                  <el-tag :type="scope.row.payment_status === 'paid' ? 'success' : 'danger'">
                    {{ scope.row.payment_status }}
                  </el-tag>
                </template>
              </el-table-column>
              <el-table-column prop="created_at" label="报名时间" width="180" />
              <el-table-column label="操作" width="150">
                <template #default="scope">
                  <el-button type="primary" size="small" @click="handleView(scope.row)">
                    查看
                  </el-button>
                  <el-button type="danger" size="small" @click="handleDelete(scope.row.id)">
                    删除
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-card>
        </div>

        <!-- 新闻管理 -->
        <div v-if="activeMenu === 'news'" class="content-body">
          <el-card>
            <template #header>
              <div class="card-header">
                <span>新闻列表</span>
                <el-button type="primary" size="small">
                  <el-icon><Plus /></el-icon>
                  发布新闻
                </el-button>
              </div>
            </template>
            <el-table :data="newsList" style="width: 100%" stripe>
              <el-table-column prop="id" label="ID" width="80" />
              <el-table-column prop="title" label="标题" />
              <el-table-column prop="author" label="作者" width="120" />
              <el-table-column prop="is_published" label="状态">
                <template #default="scope">
                  <el-switch
                    v-model="scope.row.is_published"
                    active-color="#13ce66"
                    inactive-color="#ff4949"
                    @change="handleNewsStatusChange(scope.row)"
                  />
                </template>
              </el-table-column>
              <el-table-column prop="created_at" label="发布时间" width="180" />
              <el-table-column label="操作" width="150">
                <template #default="scope">
                  <el-button type="primary" size="small" @click="handleEditNews(scope.row)">
                    编辑
                  </el-button>
                  <el-button type="danger" size="small" @click="handleDeleteNews(scope.row.id)">
                    删除
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-card>
        </div>

        <!-- 师资管理 -->
        <div v-if="activeMenu === 'teachers'" class="content-body">
          <el-card>
            <template #header>
              <div class="card-header">
                <span>教师列表</span>
                <el-button type="primary" size="small">
                  <el-icon><Plus /></el-icon>
                  添加教师
                </el-button>
              </div>
            </template>
            <el-table :data="teachers" style="width: 100%" stripe>
              <el-table-column prop="id" label="ID" width="80" />
              <el-table-column prop="name" label="姓名" />
              <el-table-column prop="title" label="职称" />
              <el-table-column prop="courses_count" label="课程数" width="100" />
              <el-table-column prop="created_at" label="创建时间" width="180" />
              <el-table-column label="操作" width="150">
                <template #default="scope">
                  <el-button type="primary" size="small" @click="handleEditTeacher(scope.row)">
                    编辑
                  </el-button>
                  <el-button type="danger" size="small" @click="handleDeleteTeacher(scope.row.id)">
                    删除
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-card>
        </div>

        <!-- 课程管理 -->
        <div v-if="activeMenu === 'courses'" class="content-body">
          <el-card>
            <template #header>
              <div class="card-header">
                <span>课程列表</span>
                <el-button type="primary" size="small">
                  <el-icon><Plus /></el-icon>
                  添加课程
                </el-button>
              </div>
            </template>
            <el-table :data="courses" style="width: 100%" stripe>
              <el-table-column prop="id" label="ID" width="80" />
              <el-table-column prop="name" label="课程名称" />
              <el-table-column prop="price" label="价格" width="100" />
              <el-table-column prop="duration" label="时长" width="100" />
              <el-table-column prop="teacher_name" label="讲师" />
              <el-table-column prop="created_at" label="创建时间" width="180" />
              <el-table-column label="操作" width="150">
                <template #default="scope">
                  <el-button type="primary" size="small" @click="handleEditCourse(scope.row)">
                    编辑
                  </el-button>
                  <el-button type="danger" size="small" @click="handleDeleteCourse(scope.row.id)">
                    删除
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-card>
        </div>

        <!-- 用户管理 -->
        <div v-if="activeMenu === 'users'" class="content-body">
          <el-card>
            <template #header>
              <div class="card-header">
                <span>用户列表</span>
                <el-button type="primary" size="small">
                  <el-icon><Plus /></el-icon>
                  添加用户
                </el-button>
              </div>
            </template>
            <el-table :data="users" style="width: 100%" stripe>
              <el-table-column prop="id" label="ID" width="80" />
              <el-table-column prop="username" label="用户名" />
              <el-table-column prop="email" label="电子邮箱" />
              <el-table-column prop="role" label="角色">
                <template #default="scope">
                  <el-tag :type="scope.row.role === 'admin' ? 'success' : 'info'">
                    {{ scope.row.role }}
                  </el-tag>
                </template>
              </el-table-column>
              <el-table-column prop="created_at" label="创建时间" width="180" />
              <el-table-column label="操作" width="150">
                <template #default="scope">
                  <el-button type="primary" size="small" @click="handleEditUser(scope.row)">
                    编辑
                  </el-button>
                  <el-button type="danger" size="small" @click="handleDeleteUser(scope.row.id)">
                    删除
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-card>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import {
  List,
  Document,
  User,
  Collection,
  Setting,
  SwitchButton,
  Download,
  Plus
} from '@element-plus/icons-vue'

// 登录状态
const isLoggedIn = ref(false)
const loginLoading = ref(false)
const currentUser = ref('admin')

// 登录表单
const loginForm = reactive({
  username: '',
  password: ''
})

const loginRules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能少于6个字符', trigger: 'blur' }
  ]
}

const loginFormRef = ref(null)

// 登录方法
const login = () => {
  loginFormRef.value.validate((valid) => {
    if (valid) {
      loginLoading.value = true
      // 模拟登录请求
      setTimeout(() => {
        if (loginForm.username === 'admin' && loginForm.password === 'admin123') {
          isLoggedIn.value = true
          currentUser.value = loginForm.username
          ElMessage.success('登录成功')
        } else {
          ElMessage.error('用户名或密码错误')
        }
        loginLoading.value = false
      }, 1500)
    }
  })
}

// 退出登录
const logout = () => {
  isLoggedIn.value = false
  loginForm.username = ''
  loginForm.password = ''
  ElMessage.success('已退出登录')
}

// 后台管理菜单
const activeMenu = ref('applications')

const handleMenuSelect = (key) => {
  activeMenu.value = key
}

const getMenuTitle = (key) => {
  const menuMap = {
    applications: '报名管理',
    news: '新闻管理',
    teachers: '师资管理',
    courses: '课程管理',
    users: '用户管理'
  }
  return menuMap[key] || '后台管理'
}

// 模拟数据
const applications = ref([
  {
    id: 1,
    name: '张三',
    phone: '13800138000',
    email: 'zhangsan@example.com',
    course: 'Web前端开发',
    status: 'pending',
    payment_status: 'unpaid',
    created_at: '2025-01-15 10:00:00'
  },
  {
    id: 2,
    name: '李四',
    phone: '13900139000',
    email: 'lisi@example.com',
    course: 'Python后端开发',
    status: 'paid',
    payment_status: 'paid',
    created_at: '2025-01-14 14:30:00'
  }
])

const newsList = ref([
  {
    id: 1,
    title: '三宁职校2025年春季招生开始',
    author: '管理员',
    is_published: true,
    created_at: '2025-01-15 10:00:00'
  },
  {
    id: 2,
    title: '学校与多家企业签订校企合作协议',
    author: '管理员',
    is_published: true,
    created_at: '2025-01-10 14:30:00'
  }
])

const teachers = ref([
  {
    id: 1,
    name: '张老师',
    title: '高级讲师',
    courses_count: 3,
    created_at: '2024-09-01 09:00:00'
  },
  {
    id: 2,
    name: '李老师',
    title: '资深讲师',
    courses_count: 2,
    created_at: '2024-09-01 09:00:00'
  }
])

const courses = ref([
  {
    id: 1,
    name: 'Web前端开发',
    price: 3999.0,
    duration: '3个月',
    teacher_name: '张老师',
    created_at: '2024-09-01 10:00:00'
  },
  {
    id: 2,
    name: 'Python后端开发',
    price: 4999.0,
    duration: '4个月',
    teacher_name: '李老师',
    created_at: '2024-09-01 10:00:00'
  }
])

const users = ref([
  {
    id: 1,
    username: 'admin',
    email: 'admin@example.com',
    role: 'admin',
    created_at: '2024-09-01 08:00:00'
  },
  {
    id: 2,
    username: 'user1',
    email: 'user1@example.com',
    role: 'user',
    created_at: '2024-09-02 10:00:00'
  }
])

// 操作方法（模拟）
const handleView = (row) => {
  console.log('查看', row)
  ElMessage.info('查看功能开发中')
}

const handleDelete = (id) => {
  console.log('删除', id)
  ElMessage.info('删除功能开发中')
}

const handleNewsStatusChange = (row) => {
  console.log('新闻状态变更', row)
  ElMessage.info('新闻状态变更功能开发中')
}

const handleEditNews = (row) => {
  console.log('编辑新闻', row)
  ElMessage.info('编辑新闻功能开发中')
}

const handleDeleteNews = (id) => {
  console.log('删除新闻', id)
  ElMessage.info('删除新闻功能开发中')
}

const handleEditTeacher = (row) => {
  console.log('编辑教师', row)
  ElMessage.info('编辑教师功能开发中')
}

const handleDeleteTeacher = (id) => {
  console.log('删除教师', id)
  ElMessage.info('删除教师功能开发中')
}

const handleEditCourse = (row) => {
  console.log('编辑课程', row)
  ElMessage.info('编辑课程功能开发中')
}

const handleDeleteCourse = (id) => {
  console.log('删除课程', id)
  ElMessage.info('删除课程功能开发中')
}

const handleEditUser = (row) => {
  console.log('编辑用户', row)
  ElMessage.info('编辑用户功能开发中')
}

const handleDeleteUser = (id) => {
  console.log('删除用户', id)
  ElMessage.info('删除用户功能开发中')
}
</script>

<style scoped>
.admin-container {
  width: 100%;
  height: 100vh;
  background-color: #f5f7fa;
}

/* 登录页面样式 */
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-card {
  width: 400px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.login-title {
  text-align: center;
  margin-bottom: 2rem;
  color: #409eff;
}

.login-form {
  max-width: 300px;
  margin: 0 auto;
}

.login-btn {
  width: 100%;
}

/* 后台管理页面样式 */
.admin-main {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

.admin-sidebar {
  width: 250px;
  background-color: #304156;
  color: #fff;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 1rem;
  border-bottom: 1px solid #435b66;
  text-align: center;
}

.sidebar-header h3 {
  margin: 0;
  color: #fff;
}

.admin-sidebar :deep(.el-menu) {
  background-color: #304156;
  border-right: none;
}

.admin-sidebar :deep(.el-menu-item) {
  color: #bfcbd9;
}

.admin-sidebar :deep(.el-menu-item.is-active) {
  color: #409eff;
  background-color: #263445;
}

.admin-sidebar :deep(.el-menu-item:hover) {
  background-color: #263445;
}

.sidebar-footer {
  margin-top: auto;
  padding: 1rem;
  border-top: 1px solid #435b66;
}

.sidebar-footer :deep(.el-button) {
  color: #bfcbd9;
  width: 100%;
  justify-content: flex-start;
}

.admin-content {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.content-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e0e0e0;
}

.content-header h2 {
  margin: 0;
  color: #2c3e50;
}

.user-info {
  font-size: 0.9rem;
  color: #666;
}

.content-body {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>