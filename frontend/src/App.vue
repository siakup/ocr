<template>
  <div class="container">
    <h1>🖼️ OCR + Ollama Demo</h1>
    <div class="upload-section">
      <input type="file" @change="handleFile" id="file-upload" />
      <label for="file-upload" class="custom-file-upload">
        <span v-if="!file">📂 Pilih Gambar</span>
        <span v-else>✅ {{ file.name }}</span>
      </label>
      <button @click="submit" :disabled="!file" class="submit-btn">
        <span v-if="loading" class="loader"></span>
        <span v-else>🚀 Proses</span>
      </button>
    </div>
    <div v-if="processTime !== null" class="process-time">
      <span>⏱️ Diproses dalam {{ processTime }} detik</span>
    </div>
    <transition name="fade">
      <div v-if="ocrText" class="result-box">
        <h3>📝 OCR Result:</h3>
        <pre class="result-text">{{ ocrText }}</pre>
      </div>
    </transition>
    <transition name="fade">
      <div v-if="llmResponse" class="result-box">
        <h3>🤖 LLM Response:</h3>
        <pre class="result-text">{{ llmResponse }}</pre>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const file = ref(null)
const ocrText = ref('')
const llmResponse = ref('')
const loading = ref(false)
const processTime = ref(null)

const handleFile = (e) => {
  file.value = e.target.files[0]
}

const submit = async () => {
  if (!file.value) return
  loading.value = true
  ocrText.value = ''
  llmResponse.value = ''
  processTime.value = null
  const formData = new FormData()
  formData.append("image", file.value)
  const start = performance.now()
  try {
    const res = await fetch("http://localhost:8000/ocr", {
      method: "POST",
      body: formData
    })
    const data = await res.json()
    ocrText.value = data.ocr_text
    llmResponse.value = data.llm_response
  } catch (e) {
    ocrText.value = 'Gagal memproses gambar.'
    llmResponse.value = ''
  } finally {
    const end = performance.now()
    processTime.value = ((end - start) / 1000).toFixed(2)
    loading.value = false
  }
}
</script>

<style scoped>
.container {
  max-width: 520px;
  margin: 48px auto;
  padding: 36px 28px;
  background: linear-gradient(135deg, #f8fafc 60%, #dbeafe 100%);
  border-radius: 20px;
  box-shadow: 0 6px 32px rgba(0,0,0,0.10);
  text-align: center;
  font-family: 'Segoe UI', 'Inter', Arial, sans-serif;
}
.upload-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  margin-bottom: 36px;
}
input[type="file"] {
  display: none;
}
.custom-file-upload {
  display: inline-block;
  padding: 12px 28px;
  background: #4f8cff;
  color: #fff;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  font-size: 1rem;
  margin-bottom: 8px;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 8px rgba(79,140,255,0.08);
}
.custom-file-upload:hover {
  background: #2563eb;
  box-shadow: 0 4px 16px rgba(37,99,235,0.10);
}
.submit-btn {
  padding: 12px 28px;
  background: linear-gradient(90deg, #22c55e 60%, #16a34a 100%);
  color: #fff;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 8px rgba(34,197,94,0.08);
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 120px;
  min-height: 44px;
}
.submit-btn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
  box-shadow: none;
}
.result-box {
  background: #f1f5f9;
  border-radius: 10px;
  padding: 20px 16px;
  margin-top: 28px;
  text-align: left;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  animation: fadeIn 0.5s;
}
.result-text {
  background: #e0e7ef;
  border-radius: 6px;
  padding: 10px;
  font-family: 'Fira Mono', 'Consolas', monospace;
  font-size: 1rem;
  white-space: pre-wrap;
  margin: 0;
}
h1 {
  color: #2563eb;
  margin-bottom: 36px;
  font-size: 2.1rem;
  letter-spacing: 1px;
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: center;
}
h3 {
  color: #0f172a;
  margin-bottom: 10px;
  font-size: 1.1rem;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.4s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: none; }
}
.loader {
  border: 3px solid #e0e7ef;
  border-top: 3px solid #2563eb;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 0.8s linear infinite;
  margin-right: 8px;
  display: inline-block;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.process-time {
  margin-bottom: 10px;
  color: #64748b;
  font-size: 1rem;
  font-style: italic;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}
</style>
