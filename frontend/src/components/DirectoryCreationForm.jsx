import * as config from '../helpers/config.js';
import { submitAction } from '../helpers/form.js';

export default DirectoryCreationForm;

function DirectoryCreationForm({ currentPath, onCreate }) {
    return (
        <form className="site-form create-directory" onSubmit={createDirectoryAction}>
            <input name="name" className="site-form_input text" placeholder="Directory Name"/>
            <button className="site-form_button">Create Directory</button>
        </form>
    );

    function createDirectoryAction(event) {
        const form = event.target;

        submitAction(form, config.url.directories, { currentPath, method: 'post', onAction: onCreate });
        event.preventDefault();
    }
}