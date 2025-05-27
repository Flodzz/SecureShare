const accountListItem = document.querySelector('.nav-links li.account');
const accountLink = accountListItem.querySelector('a');
const dropdown = accountListItem.querySelector('.dropdown-content');

let isExpanded = false;

accountLink.addEventListener('click', function(event) {
    event.preventDefault();
    isExpanded = !isExpanded;
    if (isExpanded) {
        dropdown.style.display = 'flex';
    } else {
        dropdown.style.display = 'none';
    }
    accountLink.setAttribute('aria-expanded', isExpanded);
    accountListItem.setAttribute('aria-expanded', isExpanded);
});

document.addEventListener('click', function(event) {
    if (!accountListItem.contains(event.target)) {
        dropdown.style.display = 'none';

        isExpanded = false;

        accountLink.setAttribute('aria-expanded', 'false');
        accountListItem.setAttribute('aria-expanded', 'false');
    }
});