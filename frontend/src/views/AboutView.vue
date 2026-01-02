<template>
  <div class="about-container">
    <div class="container">
      <h2>学校简介</h2>
      
      <!-- 图片轮播区域 -->
      <div class="about-carousel">
        <el-carousel :interval="3000" type="card" height="400px" arrow="hover">
          <!-- 预留的图片位置，可以根据实际情况添加或删除 -->
          <el-carousel-item>
            <div class="carousel-item">
              <el-image
                :src="BASE_URL + 'images/zhixiaodamen.jpg'"
                fit="cover"
                style="width: 100%; height: 100%;"
              >
                <template #error>
                  <div class="image-slot">
                    <el-icon><PictureFilled /></el-icon>
                    <span>学校环境图片</span>
                  </div>
                </template>
              </el-image>
            </div>
          </el-carousel-item>
          <el-carousel-item>
            <div class="carousel-item">
              <el-image
                :src="BASE_URL + 'images/shixunlou.jpg'"
                fit="cover"
                style="width: 100%; height: 100%;"
              >
                <template #error>
                  <div class="image-slot">
                    <el-icon><PictureFilled /></el-icon>
                    <span>实训设备图片</span>
                  </div>
                </template>
              </el-image>
            </div>
          </el-carousel-item>
          <el-carousel-item>
            <div class="carousel-item">
              <el-image
                :src="BASE_URL + 'images/diannaojifang.jpg'"
                fit="cover"
                style="width: 100%; height: 100%;"
              >
                <template #error>
                  <div class="image-slot">
                    <el-icon><PictureFilled /></el-icon>
                    <span>培训课堂图片</span>
                  </div>
                </template>
              </el-image>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
      
      <!-- 完整简介内容，分板块展示 -->
      <div class="full-intro">
        <!-- 学校概况板块 -->
        <section class="about-section">
          <h3>学校概况</h3>
          <div class="about-content">
            <p>枝江三宁职业技术学校（以下简称三宁职校）系政府人力资源与社会保障部门批准设立，湖北三宁化工股份有限公司投资建设的培训学校，学校创办于2013年4月，位于枝江市马家店前进路17号。</p>
          </div>
        </section>
        
        <!-- 资质认证板块 -->
        <section class="about-section">
          <h3>资质认证</h3>
          <div class="about-content">
            <p>三宁职校系湖北省安全生产教育培训机构、湖北省特种设备作业人员考试点，枝江化工安全技能实训基地、全国大学生实训实习基地、宜昌市产业工人培训基地，2023年1月被授予全国首批石油和化工行业安全技能实训基地。</p>
          </div>
        </section>
        
        <!-- 硬件设施板块 -->
        <section class="about-section">
          <h3>硬件设施</h3>
          <div class="about-content">
            <p>三宁职校占地50余亩，建筑面积31190平米，学校设置教学楼、实训大楼、办公楼、公寓住宿楼、食堂、运动场等功能分区，布局合理；建有化工工艺、机械维修、高低压电工、化工仪表自动化、金属焊接与热切割、特殊作业、安全防护和体验装置等10多个专业实训室和训练场所；拥有多媒体、OTS仿真、智慧屏等先进教学设施；学校运动场、文体健身设施、无线网络，宿舍空调、热水供应等配套设施一应俱全。</p>
          </div>
        </section>
        
        <!-- 培训项目板块 -->
        <section class="about-section">
          <h3>培训项目</h3>
          <div class="about-content">
            <p>三宁职校常年开设单位负责人、安全管理人员、电工、焊工、高处、危化等特种作业人员取证与复审培训班；开展锅炉、水处理、压力容器等特种设备操作员培训考试，开展消防值班员培训。同时为企业新入职人员、在岗员工开展钳工、电工、仪表工、焊工、化工操作工的技能提升培训和等级认定，还常年开设内训师、数字化工具应用、AI应用、Office办公技能提升等公共课程，为广大职场人职业技能提升保驾护航。</p>
          </div>
        </section>
        
        <!-- 技能大赛板块 -->
        <section class="about-section">
          <h3>技能大赛</h3>
          <div class="about-content">
            <p>三宁职校被授予技能大赛实训基地，多次承办省市级叉车、化工总控工、仪器仪表工、电工、钳工、化学检验工技能大赛，并得到各级主办单位的高度评价。</p>
          </div>
        </section>
        
        <!-- 发展规划板块 -->
        <section class="about-section">
          <h3>发展规划</h3>
          <div class="about-content">
            <p>三宁职校以赋能三宁公司和姚家港化工园区员工为主业，本着立足宜昌，辐射湖北的思路，积极对外拓展培训与相关业务。近年来为宜昌市东部产业新区、孝感东城和盐化工业园、潜江工业园、荆州松滋工业园等园区和机构提供了多工种的安全培训、专业技能提升和取证服务。未来，三宁职校将致力于打造湖北一流、行业知名、化工专业特色显著的培训学校，为化工行业发展和地方经济建设做出更大的贡献。</p>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
import { PictureFilled } from '@element-plus/icons-vue'
// 移除了交互功能相关代码
const BASE_URL = import.meta.env.BASE_URL
</script>

<style scoped>
.about-container {
  padding: 2rem 0;
  background-color: #fff;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: #2c3e50;
  font-size: 2rem;
  font-weight: 600;
}

/* 简介交互入口样式 */
.intro-entrance {
  background-color: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.intro-entrance:hover {
  background-color: #e9ecef;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

.intro-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.intro-header h3 {
  margin: 0;
  color: #409eff;
  font-size: 1.5rem;
  font-weight: 600;
}

.toggle-icon {
  font-size: 1.2rem;
  color: #409eff;
  transition: transform 0.3s ease;
  line-height: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.toggle-icon.rotate {
  transform: rotate(180deg);
}

.intro-preview {
  margin: 0;
}

.intro-preview p {
  margin: 0;
  color: #666;
  font-size: 1rem;
  line-height: 1.7;
  letter-spacing: 0.5px;
}

/* 图片轮播区域样式 */
.about-carousel {
  margin-bottom: 2rem;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.carousel-item {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 完整简介内容样式 */
.full-intro {
  background-color: #fff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

/* 内容区域样式优化 */
.about-section {
  margin-bottom: 2.5rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #f0f0f0;
}

.about-section:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.about-section h3 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  color: #409eff;
  font-size: 1.3rem;
  font-weight: 600;
  display: flex;
  align-items: center;
}

.about-section h3::before {
  content: '';
  display: inline-block;
  width: 4px;
  height: 20px;
  background-color: #409eff;
  margin-right: 10px;
  border-radius: 2px;
}

.about-content {
  width: 100%;
}

.about-content p {
  margin-bottom: 1.2rem;
  line-height: 1.8;
  color: #666;
  font-size: 1rem;
  letter-spacing: 0.5px;
  word-spacing: 1px;
}

.about-content p:last-child {
  margin-bottom: 0;
}

/* 图片占位样式 */
.image-slot {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-color: #f8f9fa;
  color: #909399;
  font-size: 1rem;
}

.image-slot span {
  margin-top: 10px;
}

.mission-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
  padding: 2rem;
  background-color: #f8f9fa;
  border-radius: 12px;
  border: 1px solid #e9ecef;
}

.mission-content {
  text-align: center;
}

.mission-content h3 {
  margin-bottom: 1rem;
  color: #409eff;
  font-size: 1.2rem;
  font-weight: 600;
}

.features-section {
  margin-bottom: 3rem;
}

.features-section h3 {
  text-align: center;
  margin-bottom: 2rem;
  color: #2c3e50;
  font-size: 1.3rem;
  font-weight: 600;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.feature-item {
  text-align: center;
  padding: 2rem;
  background-color: #f8f9fa;
  border-radius: 12px;
  transition: all 0.3s ease;
  border: 1px solid #e9ecef;
}

.feature-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
  border-color: #409eff;
}

.feature-icon {
  font-size: 2.5rem;
  color: #409eff;
  margin-bottom: 1rem;
  line-height: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.feature-item h4 {
  margin-bottom: 1rem;
  color: #2c3e50;
  font-size: 1.1rem;
  font-weight: 600;
}

.contact-section {
  padding: 2rem;
  background-color: #f8f9fa;
  border-radius: 12px;
  border: 1px solid #e9ecef;
}

.contact-section h3 {
  text-align: center;
  margin-bottom: 2rem;
  color: #2c3e50;
  font-size: 1.3rem;
  font-weight: 600;
}

.contact-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  color: #666;
  height: 2rem;
}

.contact-item span {
  font-size: 1rem;
  line-height: 2rem;
}

.contact-icon {
  color: #409eff;
  font-size: 1.2rem;
  height: 2rem;
  width: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 400px;
  background-color: #f8f9fa;
  color: #909399;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .about-container {
    padding: 1rem 0;
  }
  
  h2 {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
  }
  
  .intro-entrance {
    padding: 1.2rem;
  }
  
  .intro-header h3 {
    font-size: 1.2rem;
  }
  
  .full-intro {
    padding: 1.5rem;
  }
  
  .about-section {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .mission-section {
    grid-template-columns: 1fr;
    padding: 1.5rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .contact-info {
    grid-template-columns: 1fr;
  }
  
  .about-content p,
  .mission-content p,
  .feature-item p,
  .contact-item span {
    font-size: 0.95rem;
    line-height: 1.7;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 15px;
  }
  
  .intro-entrance {
    padding: 1rem;
  }
  
  .full-intro {
    padding: 1.2rem;
  }
  
  .about-image {
    min-width: 100%;
  }
}
</style>