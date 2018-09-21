from django.db import models

class InboxHeader(models.Model):
    msg_id  = models.PositiveIntegerField(verbose_name = 'Message ID', help_text="")
    from_id = models.PositiveIntegerField(verbose_name = 'From ID', help_text="")
    sent_date = models.DateField(verbose_name = 'sent Date')
    parent_msg_id = models.PositiveIntegerField(verbose_name = 'Parent ID', help_text="")
    subject = models.CharField(max_length=200, verbose_name = 'Message Subject')

    class Meta:
        verbose_name = 'Inbox Header'
        verbose_name_plural = 'Inbox Header'
        ordering = ["msg_id"]

    def __str__(self):
        return self.subject


class InboxBody(models.Model):
    msg_id = models.ForeignKey(InboxHeader, on_delete=models.CASCADE)
    msg_body = models.CharField(max_length=2000, verbose_name = 'Message Body')

   
class InboxRecipient(models.Model):
    READ_STATUS = ( ('R', 'READ'), ('U', 'UNREAD') , ('D','DELETED') , ('A','ARCHIVED') )
    msg_id = models.ForeignKey(InboxHeader, on_delete=models.CASCADE)
    to_id = models.PositiveIntegerField(verbose_name = 'To ID', help_text="")
    status = models.CharField(max_length=1, choices=READ_STATUS, default='U', verbose_name = 'Read Status')
    read_date = models.DateField(verbose_name = 'read Date')

    class Meta:
        verbose_name = 'Inbox Recipient'
        verbose_name_plural = 'Inbox Recipient'
        ordering = ["msg_id"]


