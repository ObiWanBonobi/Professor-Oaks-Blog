"""
View for the blog. It shows 6 posts on the main page. And when one is clicked,
will show that full post.
"""

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Shows only the published posts from the :model:`blog.Post`,
    Displays on :template:`blog/index.html`
    """

    queryset = Post.objects.filter(status=1)
    queryset = Post.objects.annotate(
        comments_count=Count("comments", distinct=True)).filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    displays on :template:`blog/post_detail.html`
    """
    # Shows the post
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    # Shows the comments
    comments = post.comments.all().order_by("created_on")
    comment_count = post.comments.filter(approved=True).count()

    # Shows the form for commenting
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, "You posted a comment")

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments, connects to the :model:`blog.Post`, and :model:`blog.Comment`
    displays on :template:`blog/post_detail.html`
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment, connects to the :model:`blog.Post`, and :model:`blog.Comment`
    displays on :template:`blog/post_detail.html`
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))
