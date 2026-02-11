Component({
  properties: {
    examData: {
      type: Array,
      value: [],
      observer: function(newVal) {
        if (newVal) this._processData(newVal);
      }
    }
  },

  data: {
    exams: []
  },

  methods: {
    _processData(data) {
      const now = new Date();
      const processed = data.map(item => {
        const targetDate = new Date(item.date);
        const diffTime = targetDate.getTime() - now.getTime();
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        
        // 模拟进度条：假设从 30 天开始倒计时
        const progress = Math.max(0, Math.min(100, (30 - diffDays) / 30 * 100));
        
        return {
          ...item,
          days: diffDays > 0 ? diffDays : 0,
          progress: diffDays > 0 ? progress : 100
        };
      });

      this.setData({ exams: processed });
    }
  }
});
