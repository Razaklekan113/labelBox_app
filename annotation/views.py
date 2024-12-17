from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import AnnotationTask

def upload_image(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')

        # Ensure that name and image are provided
        if not name or not image:
            return JsonResponse({"error": "Both name and image are required"}, status=400)

        # Create the AnnotationTask object with the uploaded image
        task = AnnotationTask.objects.create(name=name, image=image)

        # Return a response with the task ID and image URL from Cloudinary
        return JsonResponse({
            "message": "Image uploaded successfully",
            "task_id": task.id,
            "image_url": task.image.url  # Cloudinary URL will be returned here
        }, status=201)

    return render(request, 'annotation/upload_image.html')


def annotate_task(request, task_id):
    task = get_object_or_404(AnnotationTask, id=task_id)
    return render(request, 'annotation/annotate.html', {'task': task})


