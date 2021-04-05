import os
import sys


def printToFile(filename, msg):
    fd = open(filename, "a")
    fd.write("\n" + msg + "\n")
    fd.close()


def main():
    log_file = "delete_log.txt"

    printToFile(
        log_file, "Files Deleted on: /mnt/builds_mobile/buildbrain/automatic")
    findCmd = "find /mnt/builds_mobile/buildbrain/automatic -type f \( ! -iname '*.xml' \) -mtime +25 | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    printToFile(
        log_file, "Files Deleted on: /mnt/builds_mobile/buildbrain/ondemand")
    findCmd = "find /mnt/builds_mobile/buildbrain/ondemand -type f \( ! -iname '*.xml' \) -mtime +25 | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    printToFile(
        log_file, "Files Deleted on: /mnt/builds_mobile/buildbrain/virtual")
    findCmd = "find /mnt/builds_mobile/buildbrain/virtual -type f \( ! -iname '*.xml' \) -mtime +5 | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    # Delete XML files after 60 days

    findCmd = "find /mnt/builds_mobile/buildbrain/automatic -type f  -mtime +60 | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    findCmd = "find /mnt/builds_mobile/buildbrain/ondemand -type f  -mtime +60 | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    findCmd = "find /mnt/builds_mobile/buildbrain/virtual -type f  -mtime +60 | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    # to delete the logs older than 25 days older
    printToFile(log_file, "Files Deleted on: /mnt/qvslogs/")
    findCmd = "find /mnt/qvslogs/ -type f -mtime +25 | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    printToFile(log_file, "Deleting EMPTY directories.")
    findCmd = "find /mnt/builds_mobile/buildbrain/automatic -type d -empty | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    findCmd = "find /mnt/builds_mobile/buildbrain/ondemand -type d -empty | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    findCmd = "find /mnt/builds_mobile/buildbrain/virtual -type d -empty | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    findCmd = "find /mnt/qvslogs/ -type d -empty | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    findCmd = "find /mnt/builds_mobile_public/AutosanDetails/ -type d -empty | xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    # Remove files with 0 size from /mnt/builds_mobile/AutosanDetails
    printToFile(log_file, "Deleting files with ZERO size.")
    findCmd = "find /mnt/builds_mobile/AutosanDetails/ -type f -size 0| xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    findCmd = "find /mnt/builds_mobile_public/AutosanDetails/ -type f -size 0| xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    # Remove files older than 3 months from /mnt/builds_mobile/AutosanDetails
    printToFile(log_file, "Files Deleted on: /mnt/builds_mobile/AutosanDetails")
    findCmd = "find /mnt/builds_mobile/AutosanDetails/ -type f -mtime +90| xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    # Remove files older than 3 months from /mnt/builds_mobile_public/AutosanDetails/
    printToFile(
        log_file, "Files Deleted on: /mnt/builds_mobile_public/AutosanDetails/")
    findCmd = "find /mnt/builds_mobile_public/AutosanDetails/ -type f -mtime +90| xargs rm -rfv >> %s" % (
        log_file)
    os.system(findCmd)

    # Remove


if (__name__ == "__main__"):
    main()
