function openModal(index) {
    $('.modal-carousel').slick({
        prevArrow: '<button type="button" class="btn btn-link position-absolute top-50 start-0 link-underline link-underline-opacity-0 link-light z-3 btn-lg"><i class="bi bi-arrow-left"></i></button>',
        nextArrow: '<button type="button" class="btn btn-link position-absolute top-50 end-0 link-underline link-underline-opacity-0 link-light z-3 btn-lg"><i class="bi bi-arrow-right"></i></button>',
    });
    $('.modal-carousel').slick(
        "slickGoTo", index
    );
    const modal = new bootstrap.Modal($('#imageModal'));
    modal.show();
}


$('#imageModal').on('hidden.bs.modal', event => {
    $('.modal-carousel').slick('unslick');
});
