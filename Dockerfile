FROM selenium/standalone-chrome:latest

# =============================
# Copy needed files into image.
# =============================
COPY requirements.txt run.sh /var/opencart-automation/
COPY dp189 /var/opencart-automation/dp189

# ===============================================================
# Update apt repository, install pip3 and needed libs for python.
# ===============================================================
RUN sudo apt -y update \
    && sudo apt install -y python3-pip \
    && sudo pip3 install -r /var/opencart-automation/requirements.txt

ENTRYPOINT ["bash"]
CMD ["/var/opencart-automation/run.sh"]
