# College - 校园助手小程序 (Premium Edition) 🎓

[![Platform](https://img.shields.io/badge/Platform-WeChat%20Mini%20Program-3B82F6?style=for-the-badge&logo=wechat)](https://mp.weixin.qq.com/)
[![Renderer](https://img.shields.io/badge/Renderer-Skyline-8B5CF6?style=for-the-badge)](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)
[![UI Style](https://img.shields.io/badge/UI-Modern%20Glass-F1F5F9?style=for-the-badge)](https://github.com/Mortal915/College)

这是一款专为大学生设计的现代化校园助手小程序。项目经过深度重构，现已进化为 **Premium Edition**，不仅拥有极致的视觉美感，更在性能和跨平台适配上达到了商业级标准。

## 🌟 核心进化

### 1. 现代视觉体系 (Visual Design)
*   **玻璃拟态 (Glass-morphism)**：大量运用毛玻璃背景与柔和阴影，营造出轻盈、通透的层次感。
*   **线性简约图标 (Linear Icons)**：全量采用 3px 笔触的线性风格图标，视觉统一性极高，涵盖从 TabBar 到功能菜单的所有入口。
*   **高级配色方案**：基于 Slate Gray 与 Primary Blue 的学术风配色，专业且不失动感。

### 2. 全机型深度适配 (Platform Adaptation)
*   **智能导航栏**：自研 `navigation-bar` 组件，动态计算 iOS 状态栏与 Android 胶囊按钮位置，确保在灵动岛、打孔屏等各种异形屏下均能完美呈现。
*   **安全区域优化**：完美处理 iPhone Home Indicator 底部安全区，防止内容遮挡。

### 3. Skyline 极致性能
*   **原生级流畅**：全面适配微信最新的 Skyline 渲染引擎，摆脱 WebView 限制，拥有更接近原生的滑动动画与手势交互。
*   **局部滚动优化**：在成绩看板等复杂页面实现固定头部+局部滚动的平滑体验。

## 📸 模块概览

- **首页 (Home)**：智能时段问候、多维状态看板、线性快捷入口。
- **课表 (Schedule)**：动态时间轴布局，支持按星期筛选，自动定位今日行程。
- **成绩 (Grade)**：GPA 视觉仪表盘，支持学期切换，成绩单智能着色管理。
- **我的 (User)**：悬浮个人名片，分类功能菜单，全图标化视觉引导。

## 🛠️ 极客精神

项目内置了 `scripts/gen_icons.py` 图标生成引擎。通过 Python 算法直接生成全套线性 PNG 图标，确保资产高度可控、笔触绝对统一。

## 🚀 快速开始

1. **克隆项目**:
   ```bash
   git clone https://github.com/Mortal915/College.git
   ```
2. **导入开发者工具**:
   - 选择“导入项目”，目录指向 `College` 文件夹。
   - 确保 AppID 已正确配置，且 **“使用 Skyline 渲染引擎”** 已勾选。

---
*Developed with Modern Standards by Mortal915*
