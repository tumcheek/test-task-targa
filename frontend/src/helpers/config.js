export { 
    url,
    headers
};

const apiBaseUrl = 'http://127.0.0.1:8000/';
const url = {
    apiBase: apiBaseUrl,
    files: `${apiBaseUrl}files/`,
    root: `${apiBaseUrl}root/`,
    directories: `${apiBaseUrl}directories/`,
    search: `${apiBaseUrl}search/`
};
const headers = {
    default: {
        'Content-Type': 'application/json'
    }
};