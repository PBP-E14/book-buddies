async function getReplies() {
    var forumElement = document.getElementById("forum-data");
    var forum_id = forumElement.getAttribute("data-role");
    return fetch(`/forum/get_reply_json/${forum_id}/`).then((res) => res.json())
}

async function getUsers() {
    return fetch(`/forum/get_user_json/`).then((res) => res.json())
}

async function refreshReplies() {
    document.getElementById("reply_list").innerHTML = ""
    const replies = await getReplies()
    const users = await getUsers()

    var userElement = document.getElementById("current-user");
    var currentUser = userElement.getAttribute("data-role");
    var userRoleElement = document.getElementById("user-role");
    var userIsAdmin = userRoleElement.getAttribute("data-role");
    
    let htmlString = ``
    if(replies.length > 0) {
        htmlString += `
            <h4>${replies.length} Reply</h4>
            
        `
        replies.forEach((reply) => {
            var replyUser = `${reply.fields.user}`
            var username = ``
            users.forEach((thisUser) => {
                if (thisUser.pk == replyUser) {
                    username += `${thisUser.fields.username}`
                }
            })
            if (currentUser == replyUser) {
                htmlString += `
                    <div style="float: right; width: 60%">
                        <div class="card text-bg-primary mb-3" style="width: 100%;">
                            <div class="card-header container">
                                <div class="left">Replied by: ${username}</div>
                                <div class="right">
                                    <button type="button" class="btn btn-danger btn-sm" onclick="removeReply(${reply.pk})">Delete</button>
                                </div>
                            </div>
                            <div class="card-body">
                            <p class="card-text">${reply.fields.content}</p>
                            <p class="card-text" style="text-align: end;">Replied on: ${reply.fields.created_at}</p>
                            </div>
                        </div>
                    </div>
                `
            } else {
                htmlString += `<div class="card text-bg-secondary mb-3" style="max-width: 60%;">`
                if(userIsAdmin) {
                    htmlString += `
                    <div class="card-header container">
                        <div class="left">Replied by: ${username}</div>
                        <div class="right">
                            <button type="button" class="btn btn-danger btn-sm" onclick="removeReply(${reply.pk})">Delete</button>
                        </div>
                    </div>
                    `
                } else {
                    htmlString += `<div class="card-header">Replied by: ${username}</div>`
                }
                    htmlString += `
                        <div class="card-body">
                        <p class="card-text">${reply.fields.content}</p>
                        <p class="card-text" style="text-align: end;">Replied on: ${reply.fields.created_at}</p>
                        </div>
                    </div>
                `
            }
        })
    } else {
        htmlString += `
            <div class="text-center" style="margin-block-start: 15px;">
                <h5>Belum ada balasan untuk forum ini.</h5>
            </div>
        `
    }

    document.getElementById("reply_list").innerHTML = htmlString
}

refreshReplies()

function removeForum(forum_id) {
    fetch(`/forum/remove_forum_button/${forum_id}/`, {
        method: "DELETE",
    }).then(window.location = "{% url 'show_forums' %}")
    return false
}

function addReply() {
    var id_forum = `{{ forum.pk }}`
    fetch(`/forum/add_reply_ajax/${id_forum}/`, {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshReplies)

    document.getElementById("form").reset()
    return false
}

function removeReply(forum_id) {
    fetch(`/forum/remove_reply_button/${forum_id}/`, {
        method: "DELETE",
    }).then(refreshReplies)
    return false
}

function closeModal() {
    document.getElementById("form").reset()
    return false
}

document.getElementById("button_add").onclick = addReply
document.getElementById("button_close").onclick = closeModal