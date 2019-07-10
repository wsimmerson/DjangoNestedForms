from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, reverse

from . import models
from . import forms

# Create your views here.


def manage_children(request, pk):
    """Edit children and their addresses for a single parent."""

    parent = get_object_or_404(models.Parent, id=pk)

    if request.method == 'POST':
        formset = forms.ChildrenFormset(request.POST, instance=parent)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('nestedforms:manage_children', kwargs={"pk": parent.id}))
    else:
        formset = forms.ChildrenFormset(instance=parent)

    return render(request, 'manage_children.html', {
                  'parent': parent,
                  'children_formset': formset})
