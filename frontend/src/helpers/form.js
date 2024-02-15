import * as config from '../helpers/config.js';
export { submitAction };

function submitAction(form, url, { method, currentPath, onAction }) {
    const formData = new FormData(form);
    const formDataJson = JSON.stringify(Object.fromEntries(formData));
    const actionUrl = new URL(url);
    const requestOptions = {
        method,
        headers: config.headers.default,
        body: formDataJson
    };
    const onActionSuccess = (responseData) => {
        onAction(responseData);
        form.reset();
    };

    currentPath && actionUrl.searchParams.set('path', currentPath);
    fetch(actionUrl, requestOptions)
        .then(response => response.json(), console.error)
        .then(onActionSuccess);
}