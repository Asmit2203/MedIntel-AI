import axios from "axios";

const API = axios.create({
  baseURL: "https://medintel-ai-m7bn.onrender.com",
});

export const uploadReport = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await API.post(
    "/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

export const getHistory = async () => {
  const response = await API.get("/history");
  return response.data;
};

export default API;