async function getForums(choice) {
    return fetch(`/forum/get_forum_json/${choice}/`).then((res) => res.json())
}

async function getUsers() {
    return fetch(`/forum/get_user_json/`).then((res) => res.json())
}

async function refreshForums() {
    document.getElementById("forum_table").innerHTML = ""

    var radioButtons = document.getElementsByName("vbtn-radio");
    // Initialize a variable to store the selected value
    var selectedValue = "";
    // Iterate through the radio buttons to find the selected one
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            selectedValue = radioButtons[i].value;
            break;  // Exit the loop when a selected radio button is found
        }
    }
    const forums = await getForums(selectedValue)

    const users = await getUsers()
    var userRoleElement = document.getElementById("user-role");
    var userIsAdmin = userRoleElement.getAttribute("data-role");
    console.log(userIsAdmin)
    let htmlString = ``
    if (forums.length > 0) {
        htmlString += `
            <h3>Forum Discussion</h3>
            <table>
        `
        forums.forEach((forum) => {
            var forumUser = `${forum.fields.user}`
            var username = ``
            users.forEach((thisUser) => {
                if (thisUser.pk == forumUser) {
                    username += `${thisUser.fields.username}`
                }
            })
            htmlString += `
            <tr class="table-row-button">
                <td id="reply-info" onclick ="window.location='read_forum/${forum.pk}/';" style="width: 5%">
                    <p>Reply 
                    <br>${forum.fields.total_reply}
                    </p>
                </td>
                <td onclick ="window.location='read_forum/${forum.pk}/';">
                    <h5>${forum.fields.title}</h5>
                    <h6>Posted by ${username} on ${forum.fields.created_at}</h6>
            `
            if (forum.fields.content.length > 300) {
                var slicedContent = `${forum.fields.content}`.slice(0,300)
                htmlString += `
                    <p>${slicedContent}...</p>
                `
            } else {
                htmlString += `
                    <p>${forum.fields.content}</p>
                `
            }
            htmlString += `</td>`
            if (userIsAdmin == `True`) {
                htmlString += `
                    <td>
                        <a>
                            <button type="button" class="btn btn-outline-danger" onclick="removeForum(${forum.pk})">Delete</button>
                        </a>
                    </td>
                `
            }
            htmlString += `</tr>`
        })
        htmlString += `
            </table>
            <div class="text-center">
                <button type="button" class="btn btn-outline-primary btn-lg" data-bs-toggle="modal" data-bs-target="#exampleModal" style="margin-block-start: 15px;">
                    Add Forum
                </button>
            </div>
        `
    } else {
        htmlString += `
            <div class="text-center">
                <h3>Belum ada forum yang di post.</h3>
                <button type="button" class="btn btn-outline-primary btn-lg" data-bs-toggle="modal" data-bs-target="#exampleModal" style="margin-block-start: 15px;">
                    Tambah Forum
                </button>
            </div>
        `
    }

    document.getElementById("forum_table").innerHTML = htmlString
}

refreshForums()

function addForum() {
    fetch(`/forum/add_forum_ajax/`, {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshForums)

    document.getElementById("form").reset()
    return false
}

function closeModal() {
    document.getElementById("form").reset()
    return false
}

function removeForum(forum_id) {
    fetch(`/forum/remove_forum_button/${forum_id}/`, {
        method: "DELETE",
    }).then(refreshForums)
    return false
}

function selectForums(choice){
    refreshForums()
    document.getElementById(`vbtn-radio${choice}`).checked = true
    return false
}

document.getElementById("button_add").onclick = addForum
document.getElementById("button_close").onclick = closeModal