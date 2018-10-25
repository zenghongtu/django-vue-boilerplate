import axios from 'axios'

let $ajax = axios.create({
  baseURL: '/api',
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
});

$ajax.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  console.log(error);
  return Promise.reject(error)
});

$ajax.$fetchMessages = () => {
    return $ajax.get(`messages/`)
        .then(response => response.data)
};

$ajax.$postMessage = (payload) => {
    return $ajax.post(`messages/`, payload)
        .then(response => response.data)
};

$ajax.$deleteMessage = (msgId) => {
    return $ajax.delete(`messages/${msgId}`)
        .then(response => response.data)
};

export default $ajax
