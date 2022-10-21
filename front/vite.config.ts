import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@material-ui/styled-engine': '@material-ui/styled-engine-sc'
    }
  }
})
