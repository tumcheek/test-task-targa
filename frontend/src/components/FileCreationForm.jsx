import * as config from '../helpers/config.js';
import { submitAction } from '../helpers/form.js';

export default FileCreationForm;

function FileCreationForm({ currentPath, onCreate }) {
    return (
        <form className="site-form create-file" onSubmit={createFileAction}>
            <input name="name" className="site-form_input text" placeholder="File Name"/>
            <textarea name="content" className="site-form_input textarea" placeholder="File Content"></textarea>
            <button className="site-form_button">Create File</button>
        </form>
    );

    function createFileAction(event) {
        const form = event.target;

        submitAction(form, config.url.files, { currentPath, method: 'post', onAction: onCreate });
        event.preventDefault();
    }
}