<template>
  <div class="apply-container">
    <div class="container">
      <h2>在线报名</h2>
      <p class="apply-intro">请填写以下信息进行报名，我们将尽快与您联系。</p>

      <el-card class="apply-card">
        <el-form
          :model="applyForm"
          :rules="rules"
          ref="applyFormRef"
          label-width="120px"
          class="apply-form"
        >
          <el-form-item label="姓名" prop="name">
            <el-input v-model="applyForm.name" placeholder="请输入您的姓名" />
          </el-form-item>

          <el-form-item label="手机号码" prop="phone">
            <el-input v-model="applyForm.phone" placeholder="请输入您的手机号码" />
          </el-form-item>

          <el-form-item label="电子邮箱" prop="email">
            <el-input v-model="applyForm.email" placeholder="请输入您的电子邮箱" />
          </el-form-item>

          <el-form-item label="选择课程" prop="course_id">
            <el-select v-model="applyForm.course_id" placeholder="请选择您要报名的课程">
              <el-option
                v-for="course in courses"
                :key="course.id"
                :label="course.name"
                :value="course.id"
              >
                <div class="option-content">
                  <span>{{ course.name }}</span>
                  <span class="option-price">¥{{ course.price }}</span>
                </div>
              </el-option>
            </el-select>
          </el-form-item>

          <el-form-item label="备注信息">
            <el-input
              v-model="applyForm.remark"
              type="textarea"
              :rows="4"
              placeholder="请输入备注信息（可选）"
            />
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitApply" :loading="submitting">
              提交报名
            </el-button>
            <el-button @click="resetForm">重置</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </div>

    <!-- 支付对话框 -->
    <el-dialog
      v-model="paymentVisible"
      title="支付确认"
      width="50%"
      center
    >
      <div v-if="selectedCourse" class="payment-content">
        <h3>{{ selectedCourse.name }}</h3>
        <p class="course-price">¥{{ selectedCourse.price }}</p>
        <div class="payment-methods">
          <h4>选择支付方式</h4>
          <el-radio-group v-model="paymentMethod">
            <el-radio-button label="wechat">
              <el-icon><ChatLineSquare /></el-icon>
              微信支付
            </el-radio-button>
            <el-radio-button label="alipay">
              <el-icon><Wallet /></el-icon>
              支付宝
            </el-radio-button>
          </el-radio-group>
        </div>
        <div class="payment-qr" v-if="paymentMethod">
          <h4>扫描二维码支付</h4>
          <div class="qr-code">
            <el-image
              :src="paymentQrUrl"
              fit="cover"
              :preview-src-list="[paymentQrUrl]"
            >
              <template #error>
                <div class="qr-slot">
                  <el-icon><PictureFilled /></el-icon>
                </div>
              </template>
            </el-image>
          </div>
          <p class="payment-tip">请使用{{ paymentMethod === 'wechat' ? '微信' : '支付宝' }}扫描上方二维码进行支付</p>
          <el-progress :percentage="paymentProgress" :status="paymentStatus" />
        </div>
      </div>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="paymentVisible = false">取消</el-button>
          <el-button type="primary" @click="confirmPayment" :loading="paymentLoading">
            确认支付
          </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { ChatLineSquare, Wallet, PictureFilled } from '@element-plus/icons-vue'

const route = useRoute()

// 表单数据
const applyForm = reactive({
  name: '',
  phone: '',
  email: '',
  course_id: route.params.courseId || '',
  remark: ''
})

// 表单验证规则
const rules = {
  name: [
    { required: true, message: '请输入您的姓名', trigger: 'blur' },
    { min: 2, max: 20, message: '姓名长度在 2 到 20 个字符', trigger: 'blur' }
  ],
  phone: [
    { required: true, message: '请输入您的手机号码', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号码', trigger: 'blur' }
  ],
  email: [
    { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
  ],
  course_id: [
    { required: true, message: '请选择您要报名的课程', trigger: 'change' }
  ]
}

// 表单引用
const applyFormRef = ref(null)

// 提交状态
const submitting = ref(false)

// 课程列表
const courses = ref([
  {
    id: 1,
    name: 'Web前端开发',
    price: 3999.0
  },
  {
    id: 2,
    name: 'Python后端开发',
    price: 4999.0
  },
  {
    id: 3,
    name: 'UI/UX设计',
    price: 3999.0
  },
  {
    id: 4,
    name: 'Java开发',
    price: 4999.0
  },
  {
    id: 5,
    name: '数据分析',
    price: 3599.0
  },
  {
    id: 6,
    name: '平面设计',
    price: 2999.0
  }
])

// 支付相关
const paymentVisible = ref(false)
const paymentMethod = ref('wechat')
const paymentQrUrl = ref('https://picsum.photos/300/300?random=100')
const paymentProgress = ref(0)
const paymentStatus = ref('')
const paymentLoading = ref(false)
const selectedCourse = ref(null)

// 重置表单
const resetForm = () => {
  applyFormRef.value.resetFields()
}

// 提交报名
const submitApply = () => {
  applyFormRef.value.validate((valid) => {
    if (valid) {
      submitting.value = true
      
      // 模拟提交数据
      setTimeout(() => {
        // 找到选中的课程
        selectedCourse.value = courses.value.find(course => course.id === applyForm.course_id)
        if (selectedCourse.value) {
          // 显示支付对话框
          paymentVisible.value = true
          // 模拟支付进度
          startPaymentProgress()
        }
        submitting.value = false
        ElMessage.success('报名信息提交成功，请进行支付')
      }, 1500)
    } else {

      return false
    }
  })
}

// 开始支付进度模拟
const startPaymentProgress = () => {
  paymentProgress.value = 0
  paymentStatus.value = ''
  const timer = setInterval(() => {
    paymentProgress.value += 10
    if (paymentProgress.value >= 100) {
      clearInterval(timer)
      paymentStatus.value = 'success'
      setTimeout(() => {
        ElMessage.success('支付成功！')
        paymentVisible.value = false
        // 重置表单
        resetForm()
      }, 1000)
    }
  }, 500)
}

// 确认支付
const confirmPayment = () => {
  paymentLoading.value = true
  // 模拟支付请求
  setTimeout(() => {
    paymentLoading.value = false
    ElMessage.success('支付请求已提交，请等待支付结果')
  }, 1500)
}

// 页面加载时，如果有courseId参数，自动选择对应课程
onMounted(() => {
  if (route.params.courseId) {
    const courseId = parseInt(route.params.courseId)
    applyForm.course_id = courseId
  }
})
</script>

<style scoped>
.apply-container {
  padding: 2rem 0;
  background-color: #fff;
}

.apply-intro {
  text-align: center;
  margin-bottom: 3rem;
  color: #666;
  font-size: 1.1rem;
}

.apply-card {
  max-width: 800px;
  margin: 0 auto;
}

.apply-form {
  max-width: 600px;
  margin: 0 auto;
}

.option-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.option-price {
  color: #e6a23c;
  font-weight: bold;
}

.payment-content {
  text-align: center;
}

.course-price {
  font-size: 2rem;
  color: #e6a23c;
  font-weight: bold;
  margin: 1rem 0 2rem 0;
}

.payment-methods {
  margin-bottom: 2rem;
}

.payment-methods h4 {
  margin-bottom: 1rem;
  text-align: left;
}

.payment-qr {
  margin-top: 2rem;
}

.payment-qr h4 {
  margin-bottom: 1rem;
  text-align: left;
}

.qr-code {
  width: 300px;
  height: 300px;
  margin: 0 auto 1rem auto;
  border: 1px solid #e0e0e0;
  padding: 1rem;
  border-radius: 8px;
}

.qr-code :deep(.el-image) {
  width: 100%;
  height: 100%;
}

.payment-tip {
  color: #666;
  margin-bottom: 1rem;
}

.qr-slot {
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