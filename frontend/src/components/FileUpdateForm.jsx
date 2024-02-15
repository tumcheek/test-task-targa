import * as config from '../helpers/config.js';
import { entityPath } from '../helpers/utils.js';

export default FileUpdateForm;

function FileUpdateForm({ fileData, currentPath, onUpdate }) {
    return (
        <form className="site-form filesystem_actions" onSubmit={updateFileAction}>
            <textarea name="content" className="site-form_input textarea" defaultValue={fileData.content}></textarea>
            <button className="site-form_button">Save</button>
        </form>
    );

    function updateFileAction(event) {
        const form = event.target;
        const formData = new FormData(form);
        const formDataJson = JSON.stringify(Object.fromEntries(formData));
        const actionUrl = entityPath(fileData.name, { type: 'file', currentPath });
        const requestOptions = {
            method: 'PUT',
            headers: config.headers.default,
            body: formDataJson
        };

        fetch(actionUrl, requestOptions)
            .then(onResponse)
            .catch(console.error)
            .finally(() => onUpdate(formData.get('content')));
        event.preventDefault();
    };
}

function onResponse(response) {
    if (!response.ok) {
        throw new Error(response.statusText);
    }
    
    return response.json();
}