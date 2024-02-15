import { useSearchParams } from "react-router-dom";
import * as config from '../helpers/config.js';

export default SearchForm;

function SearchForm({ onSearch }) {
    const [searchParams, setSearchParams] = useSearchParams();

    return (
        <form className="site-form search" onSubmit={searchAction}>
            <input name="search_name" className="site-form_input text" placeholder="Search"/>
            <button className="site-form_button search fas fa-search"></button>
        </form>
    );

    function searchAction(event) {
        const form = event.target;
        const formData = new FormData(form);
        const searchUrl = new URL(config.url.search);

        searchUrl.pathname += formData.get('search_name');
        fetch(searchUrl)
            .then(response => response.json())
            .then(onSearch)
            .catch(console.error);
        event.preventDefault();
    }

    function onSearch(result) {
        if (result.detail) return;

        result.is_file 
            ? setSearchParams(result)
            : setSearchParams({ 'path': result.path });
    }
}